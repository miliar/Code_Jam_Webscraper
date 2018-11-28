#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

int honest(vector<double> A, vector<double> B){
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  int ans = 0, N = A.size();

  vector<bool> used(N, false);
  for(int i = 0; i < N; i++){
    int pos = -1;
    for(int j = 0; j < N; j++) if(A[i]<B[j]&&!used[j]){pos = j; break;}
    if(pos == -1) for(int j = 0; j < N; j++) if(!used[j]) {pos = j; break;}
    used[pos] = true;
    ans += (A[i]>B[pos]?1:0);
  }
  return ans;
}

int take_in(vector<double> A, vector<double> B){
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  int N = A.size();
  int ans = 0;
  do{
    int tmp = 0;
    for(int i = 0; i < N; i++) tmp += (A[i]>B[i]?1:0);
    ans = max(ans, tmp);
  }while(next_permutation(B.begin(), B.end()));
  return ans;
}

int main(){
  int T;
  cin >> T;
  for(int tc = 0; tc < T; tc++){
    int n;
    cin >> n;
    vector<double> A(n), B(n);
    for(int i = 0; i < n; i++) cin >> A[i];
    for(int i = 0; i < n; i++) cin >> B[i];
    cout << "Case #" << tc+1 << ": " << take_in(A,B) << " " << honest(A,B) << endl;
  }
  return 0;
}
