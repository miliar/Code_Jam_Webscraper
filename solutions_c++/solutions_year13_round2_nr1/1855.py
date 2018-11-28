#include<iostream>
#include<vector>
#include<algorithm>
 
using namespace std;
 
int main()
{
    int t=0;
 FILE *fp = fopen("ans.txt","w");
        cin>>t;
        int N,A;
        int k;
        vector<int> vec;
        int count=0;
        int mincount;
        for(int j=0;j<t;j++)
        {
                cin>>A>>N;
                count=N;
                mincount=N;
                for(int i=0;i<N;i++)
                {
                        cin>>k;
                        vec.push_back(k);
                }
                sort(vec.begin(),vec.end());
 
                for(int i=0;i<vec.size();)
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
                        if(count<mincount)mincount=count;
                }
                fprintf(fp,"Case #%d: %d\n",j+1,mincount);
                //cout<<"Case #"<<j+1<<": "<<mincount<<endl;
                vec.clear();
        }
        fclose(fp);
        return 0;
}
