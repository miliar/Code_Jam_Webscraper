#include <stdio.h>
#include <cstdlib>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *outf = fopen("output.txt","w");
    int t;
    vector<int> a1;
    vector<int> a2;
    fscanf(in,"%d",&t);
    
    for(int i=0; i<t; i++)
    {
            for(int j=0; j<2; j++)
            {
                    int r;
                    fscanf(in,"%d",&r);
                    for(int k=0; k<4; k++)
                    {
                                    int a,b,c,d;
                                    fscanf(in,"%d%d%d%d",&a,&b,&c,&d);
                                    if(k+1 == r && j==0)
                                    {
                                         a1.push_back(a); a1.push_back(b); a1.push_back(c); a1.push_back(d);
                                    } else if(k+1==r){
                                           a2.push_back(a); a2.push_back(b); a2.push_back(c); a2.push_back(d);
                                    }
                    }
            }
            
            vector<int> ans;
            for(int p=0; p<4; p++){
                    int res = a1[p];
                for(int q=0; q<4; q++)
                {
                    if(a2[q] == res) ans.push_back(res);
                }
            }
            fprintf(outf,"Case #%d: ",i+1);
            if(ans.size() == 0) fprintf(outf,"Volunteer cheated!\n");
            else if(ans.size() == 1) fprintf(outf,"%d\n",ans[0]);
            else fprintf(outf,"Bad magician!\n");
            a1.clear();
            a2.clear();
            
    }
    
}
