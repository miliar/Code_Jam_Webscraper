#include <iostream>
#include <string>     // std::string, std::to_string
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

vector<bool> Pancakes;

void Str2bool (string in_str)
{
    Pancakes = vector<bool> (in_str.length() , false);

    for (int i=0; i<in_str.length() ; i++)
        if (in_str[i] == '+') Pancakes[i] = true;
}

void PrintPank ()
{
    for (int i=0; i<Pancakes.size() ; i++)
        cout << ( Pancakes[i] ? "+" : "-" );
    cout << endl;
}

void flip_pan_at (int position)
{
    if (position < 0) cout << "ERROR 1";
    if (position >= Pancakes.size()) cout << "ERROR 2";

    vector<bool> copy_pank = Pancakes;
    int L = Pancakes.size();

    for (int i=0; i<= position; i++)
        copy_pank[i] =  ! (Pancakes [position-i]);

    Pancakes = copy_pank;
}

bool is_pank_happy()
{
    bool ans = true;

    for (int i=0; i<Pancakes.size() ; i++)
        ans = ans && Pancakes[i];

    return ans;
}

int make_pank_happy ()
{
    int repetition = 0;

    while (!is_pank_happy())
    {
        int find_first_block= 0;

        for (int i=0; i<Pancakes.size() ; i++)
            if (Pancakes[i] == Pancakes[0])
                find_first_block = i;
            else
                break;
        //cout << "block = " << find_first_block << endl;
        flip_pan_at(find_first_block);
        //cout << ": " ;
        //PrintPank();


        repetition++;
    }

    return repetition;
}

int main ()
{

  int CaseCount;
  cin >> CaseCount;

  for (int cc=0; cc<CaseCount ; cc++)
  {
    string input;
    cin >> input;


    cout << "Case #" << (cc+1) << ": " ;
    Str2bool(input);
    //PrintPank();
    cout << make_pank_happy();

    //cout << input;

    cout << endl;
  }



  return 0;
}
