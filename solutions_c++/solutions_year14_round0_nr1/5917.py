 #include <iostream>
using namespace std;
int main() {
  int C,c;
  cin >> C;
  for(c=1; c<=C; c++) {
    int row,i,j,n,ans=0,ansnum=0;
    int nums[17] = {0};
    cin >> row;
    for(i=1;i<row;i++) for(j=0;j<4;j++) cin >> n; // discard unimportant lines
    for(i=0;i<4;i++) { cin >> n; nums[n]++; }
    for(i=row+1;i<=4;i++) for(j=0;j<4;j++) cin >> n; // discard unimportant lines

    cin >> row;
    for(i=1;i<row;i++) for(j=0;j<4;j++) cin >> n; // discard unimportant lines
    for(i=0;i<4;i++) { cin >> n; nums[n]++; if(nums[n]==2) { ans++; ansnum=n; } }
    for(i=row+1;i<=4;i++) for(j=0;j<4;j++) cin >> n; // discard unimportant lines

    cout << "Case #" << c << ": ";
    if(ans > 1) cout << "Bad magician!";
    else if(ans <= 0) cout << "Volunteer cheated!";
    else cout << ansnum;

    cout << endl;
  }
  return 0;
}