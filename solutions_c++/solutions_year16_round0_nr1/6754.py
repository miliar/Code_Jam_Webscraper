#include<bits/stdc++.h>
#include<fstream>
using namespace std;
main()
{
        unsigned long long T;
        ifstream in("in.in");
        ofstream out("output.out");
        in>>T;
        for(int z=0;z<T;z++)
        {
                unsigned long long arr[10]{};
                unsigned long long N,n;
                in>>n;
                if(n==0)
                {
                        out<<"Case #"<<z+1<<": INSOMNIA\n";
                        continue;
                }
                int i=1;
                N=n;
                while(*min_element(arr,arr+10)==0)
                {
                        if(*max_element(arr,arr+10)>99999999999)
                        {
                                out<<"Case #"<<z+1<<": INSOMNIA\n";
                                goto a;
                        }
                        while(N>0)
                        {
                                arr[N%10]+=1;
                                N=N/10;
                        }
                        i++;
                        N=n*i;
                }
                out<<"Case #"<<z+1<<": "<<n*(i-1)<<"\n";
                a:int t;
        }
        in.close();
        out.close();
}
