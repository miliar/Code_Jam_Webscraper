    #include <iostream>
    using namespace std;
     
    int main() {
    int test;
    cin>>test;
    for(int i=0;i<test;i++)
    {
    int a[4][4],b[4][4],c[4],d[4],q,w,count=0,ans;
    cin>>q;
    for(int j=0;j<4;j++)
    {
    for(int k=0;k<4;k++)
    {
    cin>>a[j][k];
    }
    }
    for(int e=0;e<4;e++)
    {
    c[e]=a[q-1][e];
    }
    cin>>w;
    for(int j=0;j<4;j++)
    {
    for(int k=0;k<4;k++)
    {
    cin>>b[j][k];
    }
    }
    for(int e=0;e<4;e++)
    {
    d[e]=b[w-1][e];
    }
    for(int j=0;j<4;j++)
    {
    for(int k=0;k<4;k++)
    {
    if(c[j]==d[k])
    {ans=c[j];
    count++;
    }
    }
    }
    if(count >1)
    cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    else if(count==0)
    cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    else
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
     
    }
    // your code goes here
    return 0;
    }