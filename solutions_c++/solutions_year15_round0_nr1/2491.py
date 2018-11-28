#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#pragma warning(disable : 4996)

using namespace std;

int main() {
    freopen("inl.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    char a[102][1002];
    int smax[102];
    for(int i = 0; i < n; ++i) {
	cin >> smax[i];
	for(int j = 0; j <= smax[i]; ++j)
	    cin >> a[i][j];
    }
    for(int i = 0; i < n; ++i)
    {
	int result = 0;
	int kol = 0;
	kol += (a[i][0] - '0');
	for(int j = 1; j <= smax[i]; ++j)
	{
	    if(kol < j)
	    {
		result = max(j-kol, result);
		kol += (a[i][j] - '0');
	    }
	    else
		kol += (a[i][j] - '0');
	}
	cout << "Case #" << i+1 << ": " << result << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}