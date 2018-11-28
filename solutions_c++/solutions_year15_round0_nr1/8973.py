#include<bits/stdc++.h>
using namespace std;
int main()
{
        int t,n,curr,i,j,add;
        char s[1002];

        /*FILE *fp = fopen("A-large.in", "r");
        FILE *fp1 = fopen ("file1.txt", "w+");

        fscanf(fp, "%d", &t);*/
        cin >> t;

        for(i=1;i<=t;i++)
        {
                //fscanf(fp, "%d %s", &n, s);
                cin>>n>>s;

                if(n == 0)
                {
                        cout << "Case #" << i <<": 0" << endl;
                        //fprintf(fp1, "Case #%d: 0\n",i);
                        continue;
                }

                add = 0;
                curr = (s[0] - '0');
                for(j=1; j<=n; j++)
                {
                        if(curr < j)
                        {
                                add += j - curr;
                                curr += j - curr + (s[j]- '0');
                        }
                        else
                                curr += (s[j]- '0');
                }
                cout << "Case #" << i <<": " << add << endl;
                //fprintf(fp1, "Case #%d: %d\n",i,add);
        }

        //fclose(fp);
        //fclose(fp1);
        return 0;
}
