
#include <fstream>
using namespace std;

int main()
{
  ifstream in("A-small-attempt2.in",ios::in);
  ofstream out("A-small-attempt2.out", ios::out);
  int casen;
  in>>casen;

  for(int casei = 0 ; casei < casen; casei ++)
  {
    int first_ans;
    int second_ans;

    int first_matrix[16];
    int second_matrix[16];

    in>>first_ans;
    for (int i = 0 ; i < 16; i ++) in>>first_matrix[i];

    in>>second_ans;
    for (int i = 0 ; i < 16; i ++) in>>second_matrix[i];


    int first_row[16];
    int second_row[16];

    for(int i = 0; i < 16 ;i ++){ first_row[i] = 0; second_row[i] = 0 ;}

    for (int i = 0 ; i < 4; i ++)
    {
      first_row[first_matrix[(first_ans-1)*4+i]-1] = 1;
      second_row[second_matrix[(second_ans-1)*4+i]-1] = 1;
    }

    int coun = 0;
    int flag = 0;

    for (int i = 0 ; i < 16; i ++)
    {
      if(first_row[i]&&second_row[i])
      {
        coun ++ ;
        flag = i;
      }
    }
    out<<"Case #" << (casei+1)<<": ";
    if(coun == 0)
    {
      out<<"Volunteer cheated!"<<endl;
    }
    else if(coun == 1)
    {
      out<<(flag+1)<<endl;
    }
    else out<<"Bad magician!"<<endl;
  }
  return 0;
}
