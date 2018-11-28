#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>

using namespace std;

double C,F,X;

double recurse ( double P )
{
	double k1, k2, past ;

	past = C / P;

	k1 = X / P;
	k2 = past + X / (P + F) ;

	if(k1 <= k2)
		return k1 ;

	else
		return past + recurse(P + F);
}


int main()
{
    fstream fin,fout;
	int tc,t,i;
	double P, mini;


	fin.open("input.txt",ios::in);
    fout.open("output.txt",ios::out);

    freopen("output.txt", "w", stdout);

    fin>>tc;
	t=0;
	while(t++ < tc){

		fin>>C>>F>>X;

		mini = min(X / 2.0, C / 2.0 + recurse(2.0 + F) );

		cout<<"Case #"<<t<<": ";

		printf("%0.7lf\n",mini);

	}

	fin.close();
	fout.close();

	return 0;
}
