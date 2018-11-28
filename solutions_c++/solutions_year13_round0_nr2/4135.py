//compiled with g++ --std=c++11
#include <iostream>

using namespace std;

class Matrix {
public:
  Matrix(uint y,uint x) {
    _y=y;
    _x=x;
    _m = new uint[y*x];
  }

  ~Matrix() { delete [] _m; }
  uint at(uint y, uint x) const { return _m[y * _x + x]; }
  uint set(uint y, uint x, uint value) const { _m[y * _x + x] = value; }
  
  uint GetHeight() const {return _y;}
  uint GetWidth() const {return _x;}
  
  void print() const {
    for(uint y = 0; y < GetHeight(); y++) {
      for(uint x = 0; x < GetWidth(); x++) {
	cout << at(y,x) << ", ";
      }
      cout << endl;
    }
  }
  
  void fill(uint num) {
    for(uint i = 0; i < _y * _x; i++)
      _m[i]=num;
  }
  
private:
  uint _x,_y;
  uint* _m;
  
  //so nothing copies this!
  Matrix(const Matrix& other);
  Matrix(const Matrix&& other);
};

template <typename S>
uint findMax(Matrix& m, uint n, uint constant, S selector) {
  uint max = selector(m, constant, 0);
  for(uint i = 1; i < n; i++) {
    uint newnum = selector(m,constant,i);
    if(newnum > max)
      max = newnum;
  }
  return max;
}



void readTestCase(Matrix& m) {
  for(uint y = 0; y < m.GetHeight(); y++) {
    for(uint x = 0; x < m.GetWidth(); x++) {
      uint val;
      cin >> val;
      m.set(y,x, val);
    }
  }
}

template <typename S>
void cutGrass(Matrix& m, uint n, uint constant, uint value, S setter) {
  for(uint i = 0; i < n; i++) {
    
    setter(m, constant, i, value);
  }
}

bool possible(Matrix& m) {
  auto getRow = [](const Matrix& m, uint constant, uint variable) { return m.at(constant, variable); };
  auto getCol = [](const Matrix& m, uint constant, uint variable) { return m.at(variable, constant); };
  
  auto setRow = [](Matrix& m, uint constant, uint variable, uint value) { if(m.at(constant,variable)>value) m.set(constant, variable, value); };
  auto setCol = [](Matrix& m, uint constant, uint variable, uint value) { if(m.at(variable,constant)>value) m.set(variable, constant, value); };
  
  Matrix simulation(m.GetHeight(), m.GetWidth());
  simulation.fill(100);
  
  for(uint y = 0; y < m.GetHeight(); y++) {
    uint max = findMax(m, m.GetWidth(), y, getRow);
    cutGrass(simulation, m.GetWidth(), y, max, setRow);
  }
  
  for(uint x = 0; x < m.GetWidth(); x++) {
    uint max = findMax(m, m.GetHeight(), x, getCol);
    cutGrass(simulation, m.GetHeight(), x, max, setCol);
  }
  
  /*
  cout << "Input:" <<endl;
  m.print();
  cout << "Simulation:" <<endl;
  simulation.print();
  */
  
  for(uint y = 0; y < m.GetHeight(); y++) {
    for(uint x = 0; x < m.GetWidth(); x++) {
      if(m.at(y,x) != simulation.at(y,x)) return false;
    }
  }
    
  return true;
}

int main() {

  //read the input
  unsigned int nTests;
  cin >> nTests;

  for(unsigned int test = 1; test <= nTests; test++) {
    
    uint width, height;
    cin >> height >> width;
    
    Matrix m(height, width);
    readTestCase(m);
    bool p = possible(m);
    cout << "Case #" << test << ": " << (p ? "YES" : "NO") << endl;
  }

}