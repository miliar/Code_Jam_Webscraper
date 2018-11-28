#include<bits/stdc++.h>
#include<fstream>
using namespace std;
void flipp(int *arr,int pos)
{
        for(int i=0;i<pos;i++)
        {
                if(arr[i]==0)
                        arr[i]=1;
                else
                        arr[i]=0;
        }
}
using namespace std;
main()
{
        unsigned long long T;
        ifstream in("in.in");
        ofstream out("output.out");
        in>>T;
        for(int z=0;z<T;z++)
        {
                string str;
                in>>str;
                int len=str.length();
                int arr[len]{};
                for(int i=0;i<len;i++)
                {
                        if(str[i]=='+')
                                arr[i]=1;
                        else
                                arr[i]=0;
                }
                if(len==count(arr,arr+str.length(),1))
                {
                        out<<"Case #"<<z+1<<": 0\n";
                        continue;
                }
                if(len==count(arr,arr+str.length(),0))
                {
                        out<<"Case #"<<z+1<<": 1\n";
                        continue;
                }
                int j=0;
                while(len!=count(arr,arr+len,1) and count(arr,arr+len,1)!=0)
                {
                        int i=0;
                        int prev=arr[0];
                        while(prev==arr[i])
                                i++;
                        flipp(arr,i);
                        j++;
                }
                a:int zzzz;
                if(arr[0]==0)
                        j=j+1;
                out<<"Case #"<<z+1<<": "<<j<<"\n";
        }
}
