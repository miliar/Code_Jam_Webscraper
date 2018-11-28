#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    FILE *in,*out;
    in = fopen("D-large.in","r");
    out = fopen("D-small.out","w");
    if(in && out)
    {
        int t,count=1;
        fscanf(in,"%d\n",&t);
        while(t--)
        {
            int len, i, j, y=0, z=0;
            double input;
            fscanf(in,"%d\n",&len);
            vector<double> a;
            vector<double> b;
            for(i=0;i<len;i++)
            {
                fscanf(in,"%lf",&input);
                a.push_back(input);
            }
            for(i=0;i<len;i++)
            {
                fscanf(in,"%lf",&input);
                b.push_back(input);
            }
            sort(a.begin(), a.end());
            sort(b.begin(), b.end());
            i=0;
            j=0;
            while(i<len && j<len)
            {
                if(a[i]<b[j])
                {
                    i++;
                    j++;
                    z++;
                }
                else
                {
                    j++;
                }
            }
            for(i=0;i<len;i++)
            {
                if(a[0]<b[0])
                {
                    a.erase(a.begin());
                    b.pop_back();
                }
                else
                {
                    a.erase(a.begin());
                    b.erase(b.begin());
                    y++;
                }
            }
            fprintf(out, "Case #%d: %d %d\n",count++, y, len-z);
        }
        fclose(in);
        fclose(out);
    }
    return 0;
}
