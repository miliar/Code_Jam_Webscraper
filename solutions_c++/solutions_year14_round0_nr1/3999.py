//dayka
#include <iostream>
#include <vector>

using namespace std;

int main() {

    ios_base::sync_with_stdio(0);

    int a, b, c, d, i, j, k, tests, first_row, second_row, result, output;
    vector<int> propositions;
    cin >> tests;
    for(k=1 ; k<=tests ; k++)
    {
        result = 0;
        output = 0;
        cin >> first_row;
        for(i=1 ; i<=4 ; i++)
        {
            cin >> a >> b >> c >> d;
            if(first_row == i)
            {
                propositions.push_back(a);
                propositions.push_back(b);
                propositions.push_back(c);
                propositions.push_back(d);
            }
        }
        cin >> second_row;
        for(i=1 ; i<=4 ; i++)
        {
            cin >> a >> b >> c >> d;
            if(second_row == i)
            {
                for(j=0 ; j<propositions.size() ; j++)
                {
                    if(a == propositions[j])
                    {
                        result++;
                        output = a;
                    }
                    if(b == propositions[j])
                    {
                        result++;
                        output = b;
                    }
                    if(c == propositions[j])
                    {
                        result++;
                        output = c;
                    }
                    if(d == propositions[j])
                    {
                        result++;
                        output = d;
                    }
                }
            }
        }
        propositions.clear();
        cout << "Case #" << k << ": ";
        if(result == 0)
            cout << "Volunteer cheated!";
        else if(result == 1)
            cout << output;
        else
            cout << "Bad magician!";
        cout << endl;
    }

return 0;
}
