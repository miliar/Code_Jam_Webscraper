#include <bits/stdc++.h>
#define INF 1000000.0
using namespace std;
int main()
{
        int T;
        cin>>T;
        int loop;
        for(loop=1;loop<=T;loop++)
        {
                int N;
                cin>>N;
                double fp_input[N];
                double sp_input[N];
                
                int i,j,k,l;
                for(i=0;i<N;i++)
                {
                        cin>>fp_input[i];
                }
                for(i=0;i<N;i++)
                {
                        cin>>sp_input[i];
                }
                
                double fp[i];
                double sp[i];
                for(i=0;i<N;i++)
                {
                        fp[i]=fp_input[i];
                        sp[i]=sp_input[i];
                }
                
                int ans2=N;
                int ans1=0;
                int index_i=0;
                int index_j=0;
                for(i=0;i<N;i++)
                {
                        int found=0;
                        double curr_diff=INF;
                        for(j=0;j<N;j++)
                        {
                                if(fp[j]>=0.0)
                                {
                                        if(sp[i]-fp[j]>0)
                                        {
                                                found=1;
                                                if(sp[i]-fp[j] < curr_diff)
                                                {
                                                        curr_diff=sp[i]-fp[j];
                                                        index_i=i;
                                                        index_j=j;
                                                }
                                        }
                                 }
                        }
                        if(found==1)
                        {
                                ans2--;
                                fp[index_j]=-INF;
                        }
                        
                        
                }
                //cout<<ans1<<endl;
                //Initialize again
                
                index_i=0;
                index_j=0;
                for(i=0;i<N;i++)
                {
                        fp[i]=fp_input[i];
                        sp[i]=sp_input[i];
                }
                for(i=0;i<N;i++)
                {
                        int found=0;
                        double curr_diff=INF;
                        for(j=0;j<N;j++)
                        {
                                if(sp[j]>=0.0)
                                {
                                        if(fp[i]-sp[j]>0)
                                        {
                                                found=1;
                                                if(fp[i]-sp[j] < curr_diff)
                                                {
                                                        curr_diff=fp[i]-sp[j];
                                                        index_i=i;
                                                        index_j=j;
                                                }
                                        }
                                 }
                        }
                        if(found==1)
                        {
                                ans1++;
                                sp[index_j]=-INF;
                        }
                }
                printf("Case #%d: %d %d\n",loop,ans1,ans2);
                
             
        }
        return 0;
}
