#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  ifstream input("A-small-attempt0.in");
  ofstream output("output.txt");

  //string teste;

  int i, j, k;

  int t = 0;
  int row_1, row_2, ans;
  int cards_1[4], cards_2[4], card;
  string ans_text;

  input >> t;
  for (i = 0; i < t; ++i)
  {
    input >> row_1;
    //cout << "row 1 - " << row_1 << endl;
    input.ignore();
    for (j = 1; j <= 4; ++j)
      if (j != row_1)
        input.ignore(30, '\n');
      else
      {
        input >> cards_1[0] >> cards_1[1] >> cards_1[2] >> cards_1[3];
        input.ignore();
      }


    input >> row_2;
    //out << "row 2 - " << row_2 << endl;
    input.ignore();
    for (j = 1; j <= 4; ++j)
      if (j != row_2)
        input.ignore(30, '\n');
      else
      {
        input >> cards_2[0] >> cards_2[1] >> cards_2[2] >> cards_2[3];
        input.ignore();
      }


    ans = 0;
    for (j = 0; j < 4; ++j)
      for (k = 0; k < 4; ++k)
        if (cards_1[j] == cards_2[k])
        {
          ans++;
          card = cards_1[j];
        }


    if (ans == 0)
      ans_text = "Volunteer cheated!";
    else if (ans > 1)
      ans_text = "Bad magician!";
    else
      ans_text = to_string(card);

    output << "Case #" << i+1 << ": " << ans_text << endl;


    /*for(j = 0; j < 4; ++j)
      cout << cards_1[j] << ' ';
    cout << endl;
    for(j = 0; j < 4; ++j)
      cout << cards_2[j] << ' ';
    cout << endl;

    cout << "hey yop" << endl;*/
    //cout << ans_text << endl;

  }

 // while (getline(input, teste))
  //  cout << teste << endl;




  input.close();
  output.close();

  //cout << "Hello world!" << endl;
  return 0;
}
