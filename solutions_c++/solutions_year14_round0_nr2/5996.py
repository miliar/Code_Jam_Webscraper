#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <ios>
#include <vector>

/*
 * Input:
 * T : test cases
 * C F X : three real values, C=cookie farm cost, F=cookie farm production, X=goal.
 * 
 * Output:
 * Case #t: 
 * 
 * Limits:
 * T<=100
 * C<=10000
 * F<=100 
 * X<=100000
 * 
 * Notes:
 * Cookies gets "self-generated" at a reate of 2 cookies per second.
 * C = cost of cookie farm, that will produce F cookies per second.
 * goal: get X cookies.
 * 
 * Cookies gets generated as a continous function, floating.
 * 
 * Absolute relative error= 1E-6
 */

double ti(double target,double rate)
{
  return target/rate;
}

// fc=farm_cost, fr=farm rate, x=goal, ct=clock time, nc=number of cookies.
double calculate(double rate,double fc,double fr,double x,double *ct)
{
  double tc,tx,tcx,d;
  //std::cout << rate << " " << fc << " " << fr << " " << x << " " << *ct <<  std::endl;
  tc=ti(fc,rate);
  tx=ti(x,rate);
  tcx=tc+ti(x,rate+fr); // Time until goal, assuming we wait and buy the farm.
  if(tx <= tc) // will reach goal before or at the same time as buying a farm
  {
    *ct += tx;
    //std::cout << "target: " << *ct << std::endl;
    return *ct; // done, this is the target.
  }
  else
  {
    if(tcx < tx) // see if we should buy the farm
    {
      // buying the farm makes sense (time with the farm to goal is less than time *without* the farm
      *ct += tc; // advance timer until we buy the farm.
      calculate(rate+fr,fc,fr,x,ct);  // Increment rate, decrement goal (bought the farm), pass on the timer.
      return *ct; // when I come back here, I should have the answer.
    }
    // got here, tx <= tcx, means I will reach the goal faster (or at the same time) if I don't buy the farm, thus: won't buy it.
    // advance time until tx:
    *ct += tx;
    return *ct;
  }
  *ct += d;
}

int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  char n[300];
  int T,t=0;  // number of test cases.
  double C,F,X,ct,nc;
  if(argc==2)
  {
    in.open(argv[1]);
    out.open((std::string(argv[1]) + ".out").c_str(),std::ofstream::out|std::ofstream::trunc);
    std::getline(in,s); // number of test cases.
    buf.str(s);
    buf >> T;
    buf.clear();
    while(std::getline(in,s))
    {
      t++; // increment test case counter.
      buf.str(s);
      buf >> C;
      buf >> F;
      buf >> X;
      buf.clear();
      ct=0;
      nc=0;
      //std::cout << std::endl;
      calculate(2,C,F,X,&ct);
      std::snprintf(n,300,"%.7lf",ct);
      //out << "Case #" << t << ": " << std::setprecision(7) << (C/(double)3.21) << " " << F << " " << X << " " << std::endl;
      out << "Case #" << t << ": " << n << std::endl;
    }
    in.close();
    out.close();
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}


