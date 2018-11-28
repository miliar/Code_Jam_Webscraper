//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Phoom on 10/4/14.
//

#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;


double cal(double c, double f, double x, double n){
    if ( (x/n) < ((c/n)+(x/(n+f))) ) {
        return x/n;
    }else{
        return (c/n + cal(c, f, x, n+f));
    }
    
}


void think()
{
    double c,f,x,n=2.0;
    cin >> c >> f >> x;
    cout << cal(c, f, x, n) << endl;
}



int main()
{
    
	freopen("B-small-practice.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TestCase = 0;
	cin >> TestCase;
    
	for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
		cout << "Case #" << CaseID << ": ";
        cout << fixed << setprecision(7);
		think();
	}

    return 0;
}
