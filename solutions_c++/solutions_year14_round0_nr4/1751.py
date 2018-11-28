#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

  int N;
  cin >> N;
  for(int i = 1; i <= N; i++){
    int n;
    cin >> n;
    vector<double> naomi, ken;
    double temp;
    for(int j = 0; j < n; j++){
      cin >> temp;
      naomi.push_back(temp);
    }
    for(int j = 0; j < n; j++){
      cin >> temp;
      ken.push_back(temp);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    /*
    for(int j = 0; j < n; j++){
      cout << naomi[j] << " " << ken[j] << endl;
      }*/

    temp = 0;
    int sum = 0;
    for(int j = 0; temp < n; j++){
      if(naomi[j] > ken[temp]){
	j--;
      }else{
	sum++;
      }
      temp++;
    }

    sum = n-sum;
    temp = n-1;
    int ans = 0;
    for(int j = n-1; j >= 0; j--){
      while(temp >= 0){
	if(naomi[j] > ken[temp]){
	  ans++;
	  temp--;
	  break;
	}else {
	  temp--;
	}
      }
    }
    cout << "Case #" << i << ": " << ans << " " << sum << endl;
  }
  return 0;
}
