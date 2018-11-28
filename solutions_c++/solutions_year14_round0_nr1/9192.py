#include <bits/stdc++.h>

using namespace std;
#define MAX 2009
#define min(a,b) (a>b?b:a)
#define max(a,b) (a>b?a:b)
//#define OJ
#ifndef OJ
	ifstream in("input.in");
	ofstream out("output.out");
	#define cin in
	#define cout out
#endif

int main(){
   int t,T,i,j,cnt,ans1,ans2,A[5][5],hash[17],num;
   cin>>T;
   for(t=1;t<=T;t++){
       cnt=0;
       memset(hash,0,sizeof(hash));
       cin>>ans1;
       for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
            cin>>A[i][j];
        for(j=1;j<=4;j++)
            hash[A[ans1][j]]++;
        cin>>ans2;
       for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
            cin>>A[i][j];
        for(j=1;j<=4;j++)
            hash[A[ans2][j]]++;
        for(j=1;j<=16;j++)
            if(hash[j]==2){
                num = j;
                cnt++;
            }
        switch(cnt){
            case 0:
                    cout<<"Case #"<<t<<": Volunteer cheated!\n";
                    break;
            case 1:
                    cout<<"Case #"<<t<<": "<<num<<'\n';
                    break;
            default:
                    cout<<"Case #"<<t<<": Bad magician!\n";
        }       
   }
   
   return 0;
}
