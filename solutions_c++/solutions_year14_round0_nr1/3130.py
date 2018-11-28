#include<iostream>
#include<cstdio>
using namespace std;
int te;
int main()
{
    cin>>te;
    int  t = 0;
    while(t<te)
    {
	t++;        
	int f,s,a1[4][4],a2[4][4],i,j;
        cin>>f;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a1[i][j];
        cin>>s;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a2[i][j];
        int cnt = 0; int temp = 0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a1[f-1][i]==a2[s-1][j]) { cnt++; temp = a1[f-1][i]; }
        if(cnt==1) cout<<"Case #"<<t<<": "<<temp<<"\n";
        else if(cnt>1) cout<<"Case #"<<t<<": Bad magician!"<<"\n";
        else cout<<"Case #"<<t<<": Volunteer cheated!"<<"\n";
	
    }

    return 0;


}
