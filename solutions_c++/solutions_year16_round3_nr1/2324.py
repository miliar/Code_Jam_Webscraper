#include <bits/stdc++.h>

using namespace std;
typedef pair<int,int> ii;
ii vec[30];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_output.out","w",stdout);
    int t,n,x,sum;
    bool b;
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%d",&n);
        for (int i=0; i<n; i++){
            scanf("%d",&x);
            vec[i]=make_pair(x,i);
        }
        sort(vec,vec+n);
        reverse(vec,vec+n);
        printf("Case #%d:",_case);
        while (vec[0].first>0){
            sum=0;
            for (int i=0; i<n; i++){
                sum+=vec[i].first;
            }
            vec[0].first--;
            b=true;
            for (int i=0; i<n; i++){
                if (vec[i].first>(sum-1)/2)b=false;
            }
            if (b){
                printf(" %c",(char)(vec[0].second+'A'));
            }else{
                vec[0].first++;
                vec[0].first--; vec[1].first--;
                b=true;
                for (int i=0; i<n; i++){
                    if (vec[i].first>(sum-1)/2)b=false;
                }
                if (b){
                    printf(" %c%c",(char)(vec[0].second+'A'),(char)(vec[1].second+'A'));
                }else{
                    vec[0].first++; vec[1].first++;
                    printf("Error");
                }
            }
            sort(vec,vec+n);
            reverse(vec,vec+n);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
