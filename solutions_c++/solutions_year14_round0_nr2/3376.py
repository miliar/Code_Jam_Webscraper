#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
//    freopen("D:\\GCJ\\B-large.in","r",stdin);
//    freopen("D:\\GCJ\\B-large.txt","w",stdout);
    double rtime = 0;
    double p;
    double c,f,x;
    int T;
//    cin >> T;
    scanf("%d",&T);
    for (int cas=0;cas<T;cas++){
        rtime = 0;

//        cin >> c >> f >> x;
        scanf("%lf %lf %lf",&c,&f,&x);
        p = 2;
        while((x-c)*(p+f)>(p*x)){
            rtime += c/p;
            p += f;
        }
        rtime += x/p;
//        cout << "Case #"<<cas+1 << ": ";
//        cout << rtime << endl;
        printf("Case #%d: %.7f\n",cas+1,rtime);
    }
    return 0;
}
