#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int look(int *a,int n) {
    int found =0;
    for(int i=0;i<4;i++) 
        if(a[i] == n )
        {
            found =1;
            break;
        }
   return found;     
}
int main()
{
   int T;
   cin>>T;
   cin.ignore();
   for(int cases=1;cases<=T;cases++)
   {
    int a[4][4],b[4][4];
    int ans1,ans2,count = 0,ret;
        cin>>ans1;
        for(int i=0;i<4;i++)
            for(int j =0;j<4;j++)
                cin>>a[i][j];
        cin>>ans2;
        for(int i=0;i<4;i++)
            for(int j =0;j<4;j++)
                cin>>b[i][j];
        
        for(int i=0;i<4;i++) {
            if(look(a[ans1-1],b[ans2-1][i])) {
                count++;
                ret=b[ans2-1][i];
            }
        }
    cout<<"Case #"<<cases<<": ";
    if(count == 0 )
        cout<<"Volunteer cheated!"<<endl;
    else if(count == 1)
        cout<<ret<<endl;
    else cout<<"Bad magician!"<<endl;    
   }
    

    return 0;
}
