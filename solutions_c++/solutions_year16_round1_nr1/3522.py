#include <iostream>
#include <string>
#include <vector>

using namespace std;
string lastWordPossible(string testCase);
int main()
{
    int n;
    cin >> n;
    string testCase;
    string answer;
    for(int i = 0; i < n; i++)
    {
        cin >> testCase;
        cout << "Case #" << (i + 1) << ": " << lastWordPossible(testCase) << endl;
    }
}

string lastWordPossible(string testCase)
{
    string answer;
    size_t x;
    x = testCase.size();
    answer = testCase[0];
    for(size_t j = 1; j < x; j++)
    {
        if(testCase[j] >= answer[0])
        {
            answer = testCase[j] + answer;
        }
        else
        {
            answer = answer + testCase[j];
        }
    }
    return answer;
}
