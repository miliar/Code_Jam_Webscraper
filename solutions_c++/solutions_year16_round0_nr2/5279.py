/*
* @Author: ahteeGang
* @Date:   2016-04-09 16:20:47
* @Last Modified by:   ahteeGang
* @Last Modified time: 2016-04-09 16:20:57
*/

#include <iostream>
#include <stack>
#include <string>

using namespace std;

unsigned int findPancakes(string pan)
{
    stack<char> pan_f;
    stack<char> pan_s;
    stack<char> pan_temp;

    char temp = pan[0];
    bool succ = false;
    int num = 0;

    for (std::string::reverse_iterator rit = pan.rbegin(); rit != pan.rend(); ++rit)
        pan_f.push(*rit);

    do {
        succ = true;
        while (!pan_f.empty()) {
            if (pan_f.top() == '-') {
                succ = false;
                break;
            }
            pan_temp.push(pan_f.top());
            pan_f.pop();
        }
        while (!succ && !pan_temp.empty()) {
            pan_f.push(pan_temp.top());
            pan_temp.pop();
        }
        if (succ)
            break;

        while (!pan_f.empty() && temp == pan_f.top()) {
            pan_s.push(pan_f.top());
            pan_f.pop();
        }
        if (!pan_f.empty())
            temp = pan_f.top();
        else
            temp = '+';

        while (!pan_s.empty()) {
            pan_f.push(temp);
            pan_s.pop();
        }
        num++;

    } while (!succ);
    return num;
}
int main()
{
    int n;
    string pan;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> pan;
        cout << "Case #" << i + 1 << ": " << findPancakes(pan) << endl;
    }
    return 0;
}