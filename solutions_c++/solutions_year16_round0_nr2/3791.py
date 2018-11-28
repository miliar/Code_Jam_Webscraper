#include <iostream>

using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int times;
    cin >> times;
    for (int time = 1; time <= times; time ++)
    {
        string a;
        cin >> a;
        int count = 1;
        for (int i = 1; i < a.length(); i++)
        {
            if (a[i] != a[i-1])
                count ++;
        }
        if (a[a.length()-1] == '+') count --;
        printf("Case #%d: %d\n",time,count);

    }
    fclose(stdout);
    return 0;
}