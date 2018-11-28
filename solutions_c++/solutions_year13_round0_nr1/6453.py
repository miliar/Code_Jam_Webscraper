#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
#include <iostream>

using namespace::std;

int check_win(string one_line)
{
  int x_num = count(one_line.begin() ,one_line.end() , 'X');
  int o_num = count(one_line.begin() ,one_line.end() , 'O');
  int t_num = count(one_line.begin() ,one_line.end() , 'T');

  if( x_num + t_num == 4 )
    {
      return 0;
    }

  else if( o_num + t_num == 4)
    {
      return 1;
    }

  else
    {
      return 2;
    }

}

int check_draw(char bord[4][4])
{
  for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
	{
	  if(bord[i][j] == '.')
	    {
	      return 3;
	    }
	}
    }

  return 2;

}

int check_result(char bord[4][4])
{

  int res_w = 4 , res_h = 4 , res_r = 4 , res_l = 4;

  for(int i = 0; i < 4; i++)
    {
      string w , h , r , l;
      for(int j = 0; j < 4; j++)
	{
	  w += bord[i][j];
	  h += bord[j][i];
	  r += bord[j][3 - j];
	  l += bord[j][j];
	}

      res_w = check_win(w);
      res_h = check_win(h);
      res_r = check_win(r);
      res_l = check_win(l);

      if(res_w <= 1)
	{
	  return res_w;
	}
      else if(res_h <= 1)
	{
	  return res_h;
	}
      else if(res_r <= 1)
	{
	  return res_r;
	}
      else if(res_l <= 1)
	{
	  return res_l;
	}

    }

  return check_draw(bord);

}

void init_bord(char bord[4][4])
{
  for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
	{
	  cin >> bord[i][j];
	}
    }
}

int main(void)
{

  int T;

  cin >> T;

  for(int i = 0; i < T; i++)
    {
      char bord[4][4];

      init_bord(bord);

      string ans;

      switch(check_result(bord))
	{
	case 0: ans = "X won\0";break;
	  
	case 1: ans = "O won\0";break;

	case 2: ans = "Draw"; break;
	default: ans = "Game has not completed\0";
	}

      cout << "Case #" << i + 1 << ": " << ans << endl;
    }

  return 0;
}
