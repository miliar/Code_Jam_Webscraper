#include <iostream>
#include <set>
#include <sstream>
#include <string>

using namespace std;

void addToSet(set<int> &alreadySeen, string str)
{
    for(int i = 0; i < str.length(); i++)
    {
        if((int)str[i] == 48)
            alreadySeen.insert(0);
        else if((int)str[i] == 49)
            alreadySeen.insert(1);
        else if((int)str[i] == 50)
            alreadySeen.insert(2);
        else if((int)str[i] == 51)
            alreadySeen.insert(3);
        else if((int)str[i] == 52)
            alreadySeen.insert(4);
        else if((int)str[i] == 53)
            alreadySeen.insert(5);
        else if((int)str[i] == 54)
            alreadySeen.insert(6);
        else if((int)str[i] == 55)
            alreadySeen.insert(7);
        else if((int)str[i] == 56)
            alreadySeen.insert(8);
        else if((int)str[i] == 57)
            alreadySeen.insert(9);
    }
}

int countSheep(const int n, int num, int & z, set<int> & alreadySeen)
{
    stringstream ss;
    ss << num;
    string str = ss.str();

    addToSet(alreadySeen, str);

    if(alreadySeen.size() == 10)
    {
        return num;
    }

    z++;
    return countSheep(n, n * z, z, alreadySeen);
}

int main()
{
    int n, num;
    int z = 1;

    set<int> alreadySeen;

    cin >> n;

    for(int i = 0; i < n; i++)
    {
        alreadySeen.clear();
        z = 1;
        cin >> num;

        if(num == 0)
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        else
            cout << "Case #" << i + 1 << ": " << countSheep(num, num, z, alreadySeen) << endl;
    }
}
