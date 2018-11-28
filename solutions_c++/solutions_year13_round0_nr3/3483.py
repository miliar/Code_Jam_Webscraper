#include<fstream>
//#include<iostream>
using namespace std;
ifstream cin ("temp.in");
ofstream cout ("temp.out");    
int main ()
{
    int t;
    cin>>t;
    int i;
    for (i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        int a,b;
        cin>>a>>b;
        int answer=0;
        if (1>=a&&1<=b) answer++;
        if (4>=a&&4<=b) answer++;
        if (9>=a&&9<=b) answer++;
        if (121>=a&&121<=b) answer++;
        if (484>=a&&484<=b) answer++;
        cout<<answer<<endl;
    }
    return 0;
}
