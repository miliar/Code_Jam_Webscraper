#include<cstdio>
#include<iostream>
#include<map>
#include<string>

using namespace std;
void click() {
	int t;
	cin>>t;
	for (int cases=1; cases<=t; cases++) {
		double c,f,x;
		cin>>c>>f>>x;
		int m = x/f;
		double time = x/2, ftime = 0.0, now = 2.0;
		ftime += c/now;
		now += f;
		while(time > ftime+x/now) {
			time = ftime+x/now;
			ftime += c/now;
			now += f;
		}
		cout<<"Case #"<<cases<<": ";
		printf("%.7lf\n",time);//<<fixed<<setprecision(7)<<time<<endl;
	}

}

int main() {
	freopen("D:\\B-small-attempt0.in","r",stdin);
	freopen("D:\\B.out","w",stdout);
    //MagicTrick();
	click();
	//fclose(stdin);
	//fclose(stdout);
    return 0;
}
