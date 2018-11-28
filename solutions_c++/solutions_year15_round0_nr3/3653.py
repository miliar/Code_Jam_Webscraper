#include<cstdio>
#include<string>
#include<map>
#include<iostream>

using namespace std;

int quaternion[5][5] = {{0,0,0,0,0},
		       {0,1,2,3,4}, 
		       {0,2,-1,4,-3},
		       {0,3,-4,-1,2},
		       {0,4,3,-2,-1}};

map<char, int> q;
int X;

int procuraK(string line, int passado, int pos);
int procuraJ(string line, int passado, int pos);

int procuraI(string line, int passado, int pos){

  int res = 1, sinal = 0, good = 0;

  // while(res){
    while(pos < X-2){

      if(!sinal && quaternion[passado][q[line[pos]]] == 2){
	good = 1;
	break;
      }
      
      if(sinal && quaternion[passado][q[line[pos]]] == -2){
	good = 1;
	break;
      }
	
      if(sinal)
	passado = (quaternion[passado][q[line[pos]]])*-1;
      else if(!sinal)
	passado = quaternion[passado][q[line[pos]]];
      sinal = 0;
      if(passado < 0){
	sinal = 1;
	passado = passado * -1;
      }
      pos++;
    }
    if(good){
      good = 0;
      pos++;
      res = procuraJ(line, 1, pos); 
      if(!res)
	return 0;
    }
    return 1;
    //}
}

int procuraJ(string line, int passado, int pos){

  int res = 1, sinal = 0, good = 0;

  //while(res){
    while(pos < X-1){

      if(!sinal && quaternion[passado][q[line[pos]]] == 3){
	good = 1;
	break;
      }
      
      if(sinal && quaternion[passado][q[line[pos]]] == -3){
	good = 1;
	break;
      }
      
      if(sinal)
	passado = (quaternion[passado][q[line[pos]]])*-1;
      else if(!sinal)
	passado = quaternion[passado][q[line[pos]]];
      sinal = 0;
      if(passado < 0){
	sinal = 1;
	passado = passado * -1;
      }
      pos++;
    }
    if(good){
      good = 0;
      pos++;
      res = procuraK(line, 1, pos);
      if(!res)
	return 0;
    }
    
    return 1;
    //}
}

int procuraK(string line, int passado, int pos){
  int sinal = 0;

  while(pos != X-1){
    if(sinal)
      passado = (quaternion[passado][q[line[pos]]])*-1;
    else if(!sinal)
      passado = quaternion[passado][q[line[pos]]];
    sinal = 0;
    if(passado < 0){
      sinal = 1;
      passado = passado * -1;
    }
    pos++;
  }
  if((quaternion[passado][q[line[pos]]] == 4 && !sinal) || (quaternion[passado][q[line[pos]]] == -4 && sinal))
    return 0;
  return 1;
}

int main(){

  int T, R, res, no;
  string line, original;
  scanf("%d", &T);
  scanf("%d %d", &X, &R);
  q['i'] = 2;
  q['j'] = 3;
  q['k'] = 4;
  no = 0;
  while(T--){
    cin>>line;
    original = line;
    for(int i = 1; i < R; i++)
      line.append(original);
    X = line.size();
    if(line.size() < 3)
      res = 1;
    else
      res = procuraI(line, 1, 0);
    no++;
    if(!res)
      printf("Case #%d: YES\n", no);
    else
      printf("Case #%d: NO\n", no);

    if(T)
      scanf("%d %d", &X, &R);    
  }

  return 0;
}
