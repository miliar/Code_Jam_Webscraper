#include<fstream>
#include<sstream>
#include<set>
#include<vector>
#include<list>
#include<algorithm>
#include<iostream>
#define ll long long int
using namespace std;





int main()
{

    int t;
    cin>>t;



		for(int tc=1;tc<=t;tc++) {

			int shym;
			cin>>shym;
			string str;
			cin>>str;
			int ps=str[0]-'0';
			int pr=0;
			for(int i=1;i<=shym+1;i++) {
				if(str[i]!='0') {
					if(ps>=i) {
						ps+=str[i]-'0';
					}
					else {
						pr+=(i-ps);
						ps+=(i-ps);
						ps+=str[i]-'0';

					}
				}

			}

			cout<<"Case #"<<tc<<": "<<pr<<endl;

		}




    return 0;
}


