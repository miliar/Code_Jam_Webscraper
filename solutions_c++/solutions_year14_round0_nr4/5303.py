#include<iostream>
#include<vector>

using namespace std;


int main(){
	int T;
	cin >> T;

	for(int it=1; it<=T; it++){
		int N;
		cin >> N;
		vector<double> naomi;
		vector<double> ken;
		vector<bool> remNaomi(N);
		vector<bool> remKen(N);
		
		double v;

		for(int i=0; i<N; i++){
			cin >> v;
			naomi.push_back(v);
		}
		for(int i=0; i<N; i++){
			cin >> v;
			ken.push_back(v);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

/*		for(int i=0; i<N; i++){
			cout << naomi[i] << " ";
		}
		cout << endl;
		for(int i=0; i<N; i++){
			cout << ken[i] << " ";
		}
		cout << endl;
*/
		int ind=0;
//		for(int i=0; i<N; i++)
//			cout << remNaomi[i] << "  " << remKen[i] << endl;
			
//		cout << endl;
		for(int i=0; i<N; i++){
			while(ind<N && ken[i] > naomi[ind])
				ind++;


//			cout << ind << "   " << i << endl;

			remNaomi[ind] = true;
			remKen[i] = true;


			
			//trata casos que sobraram
			if(ind==(N-1)){
				break;
			}
			ind++;
		}
//		cout << endl;
		int cnt = 0;
		for(int i=0; i<N; i++){
		//	cout << remNaomi[i] << "  " << remKen[i] << endl;
			if(remNaomi[i])
				cnt++;
		}
//		cout << cnt << endl << endl;
		int cnt2=0;
		ind = 0;
		for(int i=0; i<N; i++){
			while(ind<N && naomi[i] > ken[ind])
				ind++;

		//	cout << i << "   " << ind << endl;
			
			
			if(ind>=(N))	break;
			cnt2++;
			ind++;
			
		}
		cout << "Case #" << it << ": " << cnt << " " << N-cnt2 <<endl;


	}




}
