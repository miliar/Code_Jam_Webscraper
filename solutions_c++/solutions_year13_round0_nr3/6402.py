#include<fstream>
using namespace std;
int main()
{
    ifstream in;
    ofstream out;
    in.open("cj2.in");
    out.open("ans.out");
    int arr[5]={1,4,9,121,484},t,caseno;    
    in>>t;
    caseno=t;
    while(t--)
    {
       int a,b,i,count=0;
       in>>a>>b;
       for(i=0;i<6;i++)
        if(arr[i]>=a && arr[i]<=b)
         count++;
       if(t)
       out<<"Case #"<<caseno-t<<": "<<count<<endl;
       else
       out<<"Case #"<<caseno-t<<": "<<count;       
    }
in.close();
out.close();
return 0;
}
        
