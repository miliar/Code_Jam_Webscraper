#include<iostream>
#include<fstream>


using namespace std ; 

int encode_char(char ) ; 
int decide_result(int [][4]) ; 
int row_sum(int [][4], int) ;
int col_sum(int [][4], int) ;
int diag_sum_1(int [][4]) ;
int diag_sum_2(int [][4]) ;
string print_result(int, int) ; 

int main()
{

  int case_num ; 
  char ch ; 
  int array[4][4] ; 
  int result ; 
  string s_output ; 

  ifstream input_file ("A-large.txt");
  ofstream output_file ("output_large.txt");

  input_file >> case_num ; 

  cout << " case num " << case_num<< endl;

for (int case_index = 1; case_index <= case_num; case_index ++)
 
 {

  for(int i = 0 ; i< 4 ; i++ )
    {
    for (int j = 0 ; j < 4 ; j ++)
      {
	input_file >> ch ;
	array[i][j] = encode_char(ch) ; 
      }
     }

/* debug
if (case_index == 2)
  {
  for(int i = 0 ; i< 4 ; i++ )
    {
    for (int j = 0 ; j < 4 ; j ++)
      {
cout << array[i][j] << ","  ; 
      }
cout << endl ;
     }
     }*/

  result = decide_result(array) ;


s_output = print_result(case_index,  result) ;
cout << s_output << endl ; 

output_file << s_output << endl ; 
}

output_file.close() ; 

}

int encode_char(char ch)
{

  if (ch ==  'X')
    return 1 ;

  if(ch == 'O')
    return 10 ; 

  if (ch == 'T')
    return 0 ; 

  if (ch == '.')
    return -100 ; 
}

int decide_result(int array[][4])
{

  int result = 0 ; // initize

  //check all row first
  for (int i = 0; i<4 ; i++)
    {
    if (row_sum(array, i) == 3 | row_sum(array, i) == 4 )
      {
      result = 1 ; 
return result ;
      }

    if (row_sum(array, i) == 30 | row_sum(array, i) == 40 )
      {
      result = 2 ; 
      return result ; 
       }

    if (row_sum(array, i) < 0 )
      {
       result = 3 ; 
}

    }

  //check all column
  for (int i = 0; i<4 ; i++)
    {
    if (col_sum(array, i) == 3 | col_sum(array, i) == 4 )
      {
      result = 1 ; 
return result ; 
}

    if (col_sum(array, i) == 30 | col_sum(array, i) == 40 )
      {
      result = 2 ; 
return result ; 
}

    if (col_sum(array, i) < 0 )
      {
      result = 3 ; 
}

    }

  //check  diag_1 
    if (diag_sum_1(array) == 3 | diag_sum_1(array) == 4 )
      {
      result = 1 ; 
return result ; 
}

    if (diag_sum_1(array) == 30 | diag_sum_1(array) == 40 )
      {
      result = 2 ; 
return result ; 
}

    if (diag_sum_1(array) < 0 )
      {
      result = 3 ; 
}

  //check  diag_2 
    if (diag_sum_2(array) == 3 | diag_sum_2(array) == 4 )
      {
      result = 1 ; 
return result ; 
}

    if (diag_sum_2(array) == 30 | diag_sum_2(array) == 40 )
      {
      result = 2 ; 
return result ; 
}

    if (diag_sum_2(array) < 0 )
      {
      result = 3 ; 
}

return result ; 

}


  int row_sum(int array[][4], int index)
  {

    int temp = 0 ; 
 
      for(int j = 0; j<4; j++)
	temp = temp + array[index][j] ; 

  return temp ; 
  }

  int col_sum(int array[][4], int index)
  {

    int temp = 0 ; 
 
      for(int j = 0; j<4; j++)
	temp = temp + array[j][index] ; 

  return temp ; 
  }

  int diag_sum_1(int array[][4])
  {

    int temp = 0 ; 
 
      for(int j = 0; j<4; j++)
	temp = temp + array[j][j] ; 

  return temp ; 
  }

  int diag_sum_2(int array[][4])
  {

    int temp = 0 ; 
 
      for(int j = 0; j<4; j++)
	temp = temp + array[j][3-j] ; 

  return temp ; 
  }

string print_result(int case_index, int result)
{
string s1 = "Case #"; 
string s_num = to_string(case_index); 
string win ;


s1 = s1.append( s_num) ; 
s1 = s1 + ':' ; 

if  (result == 0)
  win = " Draw" ;

if  (result == 1)
  win = " X won" ;

if  (result == 2)
  win = " O won" ;

if  (result == 3)
  win = " Game has not completed" ;

return s1 + win ; 

}
  
