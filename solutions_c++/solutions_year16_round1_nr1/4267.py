#include<iostream>
using namespace std;
string output[101];
int index;
void replaceT(string a)
{
     int i;
     string temp;
     temp.insert(0,1,a[0]);
     for(i=1;i<a.size();i++)
     {
     if(a[i]>=temp[0])
     temp.insert(0,1,a[i]);
     else
     temp.insert(temp.size(),1,a[i]);
     }
     output[index++]=temp;
}

int main()
{
    int T,i;
    string S;
    cin>>T;
    for(i=0;i<T;i++)
    {
    cin>>S;
    replaceT(S);
    }
    for(i=0;i<T;i++)
    cout<<"Case #"<<i+1<<": "<<output[i]<<endl;
    return 0;
}


