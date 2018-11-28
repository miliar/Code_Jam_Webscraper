#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 0; i<t;i++){
        int x;
        cin >> x;
        string s;
        cin >> s;

        cout<< "Case #"<<i+1<<": ";

        int su = s[0] - '0', con = 0;

        if(su == 0) con++;

		for(int j = 1; j <= x ; j++){
//			cout << "#" << j << ",su: " << su << ",con: " << con << ",s: " << s[j] << " ";
			if(su + con < j)
				con += j - su - con;
			su += s[j] - '0';
//			cout << endl <<  "#" << j << ",su: " << su << ",con: " << con << ",s: " << s[j] << endl;
//        	if(s[j] != '0'){
//        		cout << su << ":" << con << ":" << j << endl;
//				if(su + con < j){
//					con += j - su;
//				}
//				su += s[j] - '0';
//   		}
        }
		
		cout << con << endl;
    }
	return 0;
}
