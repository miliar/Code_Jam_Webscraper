#include <iostream>
#include<fstream>

using namespace std;

long long int Nlen(long long int val){
	long long int len = 1;

	if (val> 0) {
    	for (len = 0; val > 0; len++) {
        	val = val/ 10;
    	}
	}
    return len;
}

void calc(int N, int count){

	int Ar[10]={},flg=0,ck=0;
	long long ctr=1,num=0, val=0, digit=0;
	int len=0;

	ofstream File;
    File.open("Op.txt", ios::app);
    if(N==0){
			File <<"Case #"<<count<<": INSOMNIA\n";
		}
	else{
		while(flg==0){
			num=ctr*N;
			len=Nlen(num);
			if(len>1){
				while (num>0){
					digit=num%10;
					if(Ar[digit]!=1){
						Ar[digit]=1;
					}
					num=num/10;
				}
			}

			else{
				Ar[num]=1;
			}
			while(ck<=9){
				if(Ar[ck++]==0){
					flg=0;
					break;
				}
				else{ 
					flg=1;
				}
			}
			ck=0;
			ctr++;
		}
		ctr--;
		File<<"Case #"<<count<<": "<<ctr*N<<endl;
	} 
	File.close();
}


int main(){

	long long N;
	int ip=0,tp=1, flg=0;

	ifstream File;
    File.open("ip.txt");
    while(!File.eof())
    {
    		File >> ip;
    		while(tp<=ip){
				File >> N;
				calc(N, tp);
				tp++;
				N=0;
			}
		
    }

    File.close();

	
	return 0;

}