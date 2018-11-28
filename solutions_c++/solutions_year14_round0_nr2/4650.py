//source here
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
#include <string>

using namespace std;

const string ANS[3]={"", "Bad magician!", "Volunteer cheated!"};

double calcu(double c, double f, double x, double speed){
    if(x/speed>((c/speed)+x/(speed+f))){
        return c/speed+calcu(c, f, x, speed+f);
    }
    else
        return x/speed;
}
int main()
{
    FILE* fp=freopen("input.txt", "r", stdin);
    FILE* fp2=freopen("output.txt", "w", stdout);
    int cases;
    double c, f, x;
    cin>>cases;
    for(int cn=1; cn<=cases; ++cn){
        cin>>c>>f>>x;
        double res=calcu(c, f, x, 2.0);
        cout<<setprecision(7)<<fixed;
        cout<<setprecision(7)<<fixed<<"Case #"<<cn<<": "<<res<<endl;

    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
