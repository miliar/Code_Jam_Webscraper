#include<iostream>
#include<conio.h>
using namespace std;

int main(){
	int TT;
        freopen("output.out","w",stdout);
cin>>TT;
int cs=1;
while(TT--)
{
	int A1[4][4],A2[4][4];
	int ans1,ans2;
	cin>>ans1;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j)
			cin>>A1[i][j];
	}
	cin>>ans2;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j)
			cin>>A2[i][j];
	}

	//take row 1 in different array a1
//	int a1[4],a2[4];
//	for(int i=0;i<=3;++i){
//		a1[i]=A1[ans1-1][i];
//	}
//	for(int i=0;i<=3;++i){
//		a2[i]=A2[ans2-1][i];
//	}

	//find common keys from a1 and a2
	int common[4];
                         int count=0,index;
	for(int i=0;i<=3;++i){
                        for(int j=0;j<=3;++j){
                            if (A1[ans1 -1] [i] == A2[ans2 -1][j]){
                                    common[i]=     A1[ans1 -1][i];
                                    break;
                            }
                            else
                                    common[i]=100;
                        }
                      }

	//print final result
	
	for(int i=3;i>=0;--i)
                    {
		if(common[i]!=100){
			count++;
			index=i;
		}

	}
	if (count == 1){
		cout<<"Case #"<< cs++ <<": "<<common[index]<<endl;
	}
	else if (count>1){
		cout<<"Case #"<< cs++ <<": "<<"Bad magician!"<<endl;
                                        count = 0;
	}
	else if (count == 0){
		cout<<"Case #"<< cs++ <<": "<<"Volunteer cheated!"<<endl;
	}

}
fclose(stdout);
}
