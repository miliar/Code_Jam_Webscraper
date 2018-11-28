#include<cstdio>

using namespace std;

int main()
{
    //freopen("c:\\Users\\Blank\\Desktop\\B-small-attempt0.in", "r", stdin);
    //freopen("c:\\Users\\Blank\\Desktop\\B-small-attempt2.out.txt", "w", stdout);
    int n;
    while(~scanf("%d", &n)){
        int q = 0;
        while(n--){
            double c, f, x;
            scanf("%lf%lf%lf", &c, &f, &x);
            q++;
            printf("Case #%d: ", q);
            double a = 2, b, t = 0;
            int i;
            for(i = 0; ; i++){
                if(x / a > c / a + x / (a + f)){
                    t += c / a;
                    a += f;
                }
                else{
                    t += x / a;
                    break;
                }
            }
            printf("%.7lf\n", t);
        }
    }
    return 0;
}
