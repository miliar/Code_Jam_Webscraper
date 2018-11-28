#include <bits/stdc++.h>

using namespace std;

void decrease(vector<int>& c, vector<int>& d)
{
    for(int i=0; i<256; i++)
        c[i]-=d[i];
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    vector<int> zero, one, two, three, four, five, six, seven, eight, nine;
    for(int i=0; i<256; i++)
    {
        zero.push_back(0);
        one.push_back(0);
        two.push_back(0);
        three.push_back(0);
        four.push_back(0);
        five.push_back(0);
        six.push_back(0);
        seven.push_back(0);
        eight.push_back(0);
        nine.push_back(0);
    }

    zero['Z']++;
    zero['E']++;
    zero['R']++;
    zero['O']++;

    one['O']++;
    one['N']++;
    one['E']++;

    two['T']++;
    two['W']++;
    two['O']++;

    three['T']++;
    three['H']++;
    three['R']++;
    three['E']++;
    three['E']++;

    four['F']++;
    four['O']++;
    four['U']++;
    four['R']++;

    five['F']++;
    five['I']++;
    five['V']++;
    five['E']++;

    six['S']++;
    six['I']++;
    six['X']++;

    seven['S']++;
    seven['E']++;
    seven['V']++;
    seven['E']++;
    seven['N']++;

    eight['E']++;
    eight['I']++;
    eight['G']++;
    eight['H']++;
    eight['T']++;

    nine['N']++;
    nine['I']++;
    nine['N']++;
    nine['E']++;

    int tn;
    cin>>tn;
    for(int tc=1; tc<=tn; tc++)
    {
        vector<int> c;
        for(int i=0; i<256; i++)
            c.push_back(0);

        string str;
        cin>>str;
        for(int i=0; i<str.size(); i++)
            c[str[i]]++;
        vector<int> ans_former;
        for(int i=0; i<10; i++)
            ans_former.push_back(0);

        while(c['Z'])
        {
            decrease(c, zero);
            ans_former[0]++;
        }

        while(c['W'])
        {
            decrease(c, two);
            ans_former[2]++;
        }

        while(c['X'])
        {
            decrease(c, six);
            ans_former[6]++;
        }

        while(c['G'])
        {
            decrease(c, eight);
            ans_former[8]++;
        }

        while(c['U'])
        {
            decrease(c, four);
            ans_former[4]++;
        }

        while(c['F'])
        {
            decrease(c, five);
            ans_former[5]++;
        }

        while(c['I'])
        {
            decrease(c, nine);
            ans_former[9]++;
        }

        while(c['T'])
        {
            decrease(c, three);
            ans_former[3]++;
        }

        while(c['O'])
        {
            decrease(c, one);
            ans_former[1]++;
        }

        while(c['S'])
        {
            decrease(c, seven);
            ans_former[7]++;
        }

        string ans;
        for(int i=0; i<10; i++)
            for(int j=0; j<ans_former[i]; j++)
                ans.push_back('0'+i);
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
    return 0;
}
