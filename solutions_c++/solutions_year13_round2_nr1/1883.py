#include<iostream>
#include<vector>
#include<algorithm>
#define int1 long long
using namespace std;

int main()
{
    int t=0;
        cin>>t;

        int1 N,A;
        int1 k;
        vector<int1> vec;
        int1 count=0;
        int1 count1;
        for(int1 j=0;j<t;j++)
        {
                cin>>A>>N;
                count=N;

                for(int1 i=0;i<N;i++)
                {
                        cin>>k;
                        vec.push_back(k);
                }
                sort(vec.begin(),vec.end());
                count1=N;
                for(int1 i=0;i<vec.size();)
                {
                        if(vec[i]<A)
                                {A+=vec[i++];count--;}
                        else
                        {
                                if(vec[i]>=A)
                                {
                                        if(A<=1)
                                                break;
                                        A+=(A-1);
                                        count++;

                                }
                        }
                        if(count<count1)count1=count;
                }
                cout<<"Case #"<<j+1<<": "<<count1<<endl;
                vec.clear();
        }
        return 0;
}
