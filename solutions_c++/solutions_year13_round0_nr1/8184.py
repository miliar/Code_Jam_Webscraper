#ifndef __PROBLEM_1__
#define __PROBLEM_1__
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <string>
#include <iostream>

enum{ X_WON,  O_WON, DRAW, INCOMPLETE };

struct equal{
  bool unfilled ;
  
  equal():unfilled(false){}
  
  bool operator() (const char &a,  const char &b)
  {
    if (a=='.') 
    {
      unfilled = true ;
      return false ;
    }
    return (a==b) || (a == 'T') ;
  }
};

static const char xwon[] = "XXXX" ;
static const char owon[] = "OOOO" ;

struct problem1
{
  char state[4*4] ;
  int check_state()
  {
    equal eql ;
    // check rows
    for (int i = 0; i < 4; ++i)
    {
      bool tmp = true ;
      for (int k = 0; k < 4; ++k)
        if (!eql(state[4*i+k], xwon[k]))
        {
          tmp = false ;
          break ;
        }
        if (tmp)
          return X_WON ;
        
        tmp = true ;
      for (int k = 0; k < 4; ++k)
        if (!eql(state[4*i+k], owon[k]))
        {
          tmp = false ;
          break ;
        }
        if (tmp)
          return O_WON ;
    }
    // check columns
    for (int i = 0; i < 4; ++i)
    {
      bool tmp = true ;
      for (int k = 0; k < 4; ++k)
        if (!eql(state[4*k+i], xwon[k]))
        {
          tmp = false ;
          break ;
        }
        if (tmp)
          return X_WON ;
        
        tmp = true ;
      for (int k = 0; k < 4; ++k)
        if (!eql(state[4*k+i], owon[k]))
        {
          tmp = false ;
          break ;
        }
        if (tmp)
          return O_WON ;
    }
    
    //check diagonals
    bool tmp = true ;
    for (int k = 0; k < 4; ++k)
      if (!eql(state[4*k+k], owon[k]))
      {
        tmp = false ;
        break ;
      }
      if (tmp)
        return O_WON ;
      
      tmp = true ;
    for (int k = 0; k < 4; ++k)
      if (!eql(state[3*k+3], owon[k]))
      {
        tmp = false ;
        break ;
      }
      if (tmp)
        return O_WON ;
      
      tmp = true ;
    for (int k = 0; k < 4; ++k)
      if (!eql(state[4*k+k], xwon[k]))
      {
        tmp = false ;
        break ;
      }
      if (tmp)
        return X_WON ;
      
      tmp = true ;
    for (int k = 0; k < 4; ++k)
      if (!eql(state[3*k+3], xwon[k]))
      {
        tmp = false ;
        break ;
      }
      if (tmp)
        return X_WON ;  
      
      if (eql.unfilled) return INCOMPLETE ;
      else return DRAW ;
  }
  
  void read_state()
  {
    int count = 0 ;
    std::string s ;
    std::getline(std::cin, s) ; // read empty line
    for (int i = 0; i < 4; ++i)
    {
      std::getline(std::cin, s) ;
      for (int j = 0; j < 4; ++j)
        state[count++] = s[j] ;
    }
  }
  
  problem1& print_state()
  {
    for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
        std::printf("%c", state[4*i+j]) ;
      std::printf("\n") ;
    }
    return *this ;
  }
  
  problem1& do_problem1(const int i)
  {
    read_state();
    int soln = check_state() ;
    switch (soln)
    {
      case X_WON:
        std::printf("Case #%d: X won\n", i+1) ;
        break ;
      case O_WON: 
        std::printf("Case #%d: O won\n", i+1) ;
        break ;
      case INCOMPLETE:
        std::printf("Case #%d: Game has not completed\n", i+1) ;
        break ;
      case DRAW:
        std::printf("Case #%d: Draw\n", i+1) ;
        break ;
      default:
        std::fprintf(stderr,  "ERROR!\n");
    }
    
    return *this ;
  }
} ;

#endif