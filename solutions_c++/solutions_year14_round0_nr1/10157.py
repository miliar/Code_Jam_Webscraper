#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
using namespace std;
int v1[4][4],v2[4][4];
int main() {
    ios_base::sync_with_stdio(false);
    int T,row1,row2,ans,count;
    cin>>T;
    for(int a=1;a<=T;a++)
    {
        count=0;
        cin>>row1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>v1[i][j];
        cin>>row2;
        for(int i=0;i<4;i++)
           for(int j=0;j<4;j++)
               cin>>v2[i][j];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(v1[row1-1][i]==v2[row2-1][j]){
                        ans=v1[row1-1][i];
                    count++;
                }
        }
        if(count==0)
        {
            cout<<"Case #"<<a<<": Volunteer cheated!"<<endl;
        }
        else if(count==1)
        {
            cout<<"Case #"<<a<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<a<<": Bad magician!"<<endl;
        }
    }
	return 0;
}
