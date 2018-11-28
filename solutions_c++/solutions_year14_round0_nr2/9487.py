#include<iostream>
#include<cstdio>

using namespace std;
int main()
{
    int t;
    double f,x,c;
    double ans =1e9;
    double rate ,time ,t1;
    int caseno = 0;
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        int k = 0;
        //rate = 2.00;
        scanf("%lf%lf%lf",&c,&f,&x);
        time = 1e9;
        while( 1 ){
            rate = 2.00;
            t1 = 0;
            ans = time;
            for(int i = 1; i <= k; i++){
                t1 = t1 + c/rate;
                rate = f + rate;
            }
            time = t1 + (x/rate);
            if(ans<time)
            break;
        //    cout<<"time = "<<time<<endl;;
            k++;
        }
        printf("Case #%d: %.7lf\n",++caseno,ans);

    }
    return 0;
}
