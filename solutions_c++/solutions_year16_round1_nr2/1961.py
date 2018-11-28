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
                int N;
                in>>N;
                int arr[2501]{};
                int A[101][101];
                for(int i=0;i<2*N-1;i++)
                {
                       for(int j=0;j<N;j++)
                        {
                                in>>A[i][j];
                                arr[A[i][j]]++;
                        }
                }
                vector<int>vec{};
                for(int i=0;i<2501;i++)
                {
                        if(arr[i]%2==1)
                                if(count(vec.begin(),vec.end(),i)==0)
                                        vec.push_back(i);
                }
                sort(vec.begin(),vec.end());
                out<<"Case #"<<z+1<<":";
                for(int i=0;i<vec.size();i++)
                        out<<" "<<vec[i];
                out<<"\n";
                vec.clear();
        }
}
