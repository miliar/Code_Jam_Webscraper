#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main()
{ ofstream cout("ouput.txt");
 int t; cin>>t; int ans[t];
for(int i=0;i<t;i++)
{int aa; cin>>aa; aa--; int a[4][4];
for(int j=0;j<4;j++) for(int k=0;k<4;k++) cin>>a[j][k];
int bb; cin>>bb; bb--; int b[4][4];
for(int j=0;j<4;j++) for(int k=0;k<4;k++) cin>>b[j][k]; int count=0; int anss;
for(int j=0;j<4;j++)
{for(int k=0;k<4;k++)
{if(a[aa][j]==b[bb][k])
{ count++; anss=a[aa][j];}
}
}
if(count==0) ans[i]=0;
else if(count==1) ans[i]=anss;
else ans[i]=17;
}
for(int i=0;i<t;i++)
{if(ans[i]==0) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
else if(ans[i]==17) cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
else cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
}
}
