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

    ofstream myfile;
    myfile.open ("example.txt");
    //myfile << "Writing this to a file.\n";
  //myfile.close();

		for(int testCase=1;testCase<=t;testCase++) {

			int sMax;//=s.nextInt();
			cin>>sMax;
			string str;//=s.nextLine();
			cin>>str;
			int personsStanding=str[0]-'0';
			int personsRequired=0;
			for(int i=1;i<=sMax+1;i++) {
				if(str[i]!='0') {
					if(personsStanding>=i) {
						personsStanding+=str[i]-'0';
					}
					else {
						personsRequired+=(i-personsStanding);
						personsStanding+=(i-personsStanding);
						personsStanding+=str[i]-'0';

					}
				}

			}

			myfile<<"Case #"<<testCase<<": "<<personsRequired<<endl;

		}
		myfile.close();




    return 0;
}


