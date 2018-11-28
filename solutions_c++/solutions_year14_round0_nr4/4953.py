#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

class block{
public:
	block(int o,double w){
		owner = o;
		weight = w;
	}
	~block(){	}
	int owner;
	double weight;
};

void blocksort(block* b[],int size){
	int i,j;
	block* temp;
    for (i=size-1;i>0;i--)
    {
        for (j=0;j<=i-1;j++)
        {
            if (b[j]->weight<b[j+1]->weight)
            {
                temp = b[j];
                b[j] = b[j+1];
                b[j+1] = temp;
            }
        }
    }
}

int main(){
	int tt;
	cin>>tt;
	for(int ii=0;ii<tt;ii++){
		int N;
		cin>>N;
		block* blocks[2*N];
		for(int i=0;i<N;i++){
			double w;
			cin>>w;
			blocks[i] = new block(0,w);
		}
		for(int i=0;i<N;i++){
			double w;
			cin>>w;
			blocks[N+i] = new block(1,w);
		}
		blocksort(blocks,2*N);
		int war=0,dwar=0;
		int flag = 0;
		for(int i=0;i<2*N;i++){
			if(blocks[i]->owner==1)flag++;
			else if(flag>0){
				flag--;
				war++;
			}
		}
		war = N-war;
		for(int i=2*N-1;i>=0;i--){
			if(blocks[i]->owner==1)flag++;
			else if(flag>0){
				flag--;
				dwar++;
			}
		}
		cout<<"Case #"<<ii+1<<": "<<dwar<<" "<<war<<endl;
	}
}
