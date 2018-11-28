/*
 * Senate.cpp
 *
 *  Created on: May 8, 2016
 *      Author: tushar
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
	int test_case, parties;

	cin >> test_case;
	for (int i = 1; i <= test_case; ++i) {
		cin >> parties;
		vector <char> party_list;
		vector <int> party_members;
		for (int j = 0; j < parties; j++) {
			int mem_num;
			cin >>mem_num;
			if(party_list.size() == 0){
				party_list.push_back(65+j);
				party_members.push_back(mem_num);
			} else {
				bool inserted =false;
				for (int k = 0; k < party_members.size(); k++){
						if(mem_num > party_members[k]){
							party_members.insert(party_members.begin()+k, mem_num);
							party_list.insert(party_list.begin()+k, 65+j);
							inserted =true;
							break;
						}
				}
				if(!inserted){
					party_members.push_back(mem_num);
					party_list.push_back(65+j);
				}

			}


		}//Sorted entries done.

		string evac ="";
		while (party_list.size()> 1){
			while(party_members[party_members.size()-1] > 0){
				--party_members[party_members.size()-1] ;
				--party_members[party_members.size()-2] ;
				evac = string(1, party_list[party_list.size()-1])+string(1, party_list[party_list.size()-2]) + " "+evac;
			}
			party_list.pop_back();
			party_members.pop_back();
			if(party_members[party_members.size()-1] == 0){
				party_list.pop_back();
				party_members.pop_back();
			}

		}

		if((party_list.size() == 1)){
			int t = party_members[0]/2;
			for(int x=0;x<t;x++){
				evac = string(1,party_list[0]) + string(1,party_list[0]) +" "+evac;
			}
			if(party_members[0]%2 == 1){
				evac = string(1,party_list[0])+" "+evac;
			}
		}


		//print arrays
		/*
		for (int k = 0; k < party_members.size(); k++){
			cout << party_list[k] << "-" << party_members[k]<< ";" ;
		}

		cout<<endl;
		*/
		evac.erase(evac.end()-1);

		cout<<"Case #"<<i<<": "<<evac<<endl;

	}

	return 0;

}



