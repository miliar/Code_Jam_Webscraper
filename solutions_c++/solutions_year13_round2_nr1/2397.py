#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{

    long T,A,N,moves,av,here;
    bool done;
    vector<long> arr;
    cin>>T;
    for (long q=1;q<=T;q++)
    {
        cin>>A>>N;
        moves=0;
        arr=*new vector<long>();
        for (long i=0;i<N;i++)
        {
            cin>>av;
            arr.push_back(av);
        }
        sort(arr.begin(),arr.end());
        for (long i=0;i<N;i++)
        {
       
            //cout<<moves<<" "<<A<<endl;
            
            if (A<=arr[i])
            {
                here=0;
                done=false;
                while (here<(N-i))
                {
                    A+=A-1;
                    here++;
                    if (A>arr[i])
                    {
                        moves+=here;
                        done=true;
                        i--;
                        break;
                        
                    }
                }
                if (not done)
                {
                    moves+=N-i;
                    break;
                }
                
            }
            else
            {
                A+=arr[i];
            }
        }
        cout<<"Case #"<<q<<": "<<moves<<endl;
    }
}
